# Worked Example: NovaCart Checkout Audit

This is a synthetic demonstration of output quality. Its facts apply only to this example.

## Input

- Artifact: responsive checkout prototype plus a screen recording of payment submission.
- Scope: cart review through payment confirmation; account creation excluded.
- Users supplied by the project: Priya Sharma, who prioritizes fast guest checkout and immediate payment confirmation; Rohan Mehta, who prioritizes transparent totals, coupons, security, and payment-status clarity.
- Observed evidence: the final total changes after delivery selection; the Pay button remains enabled for four seconds after activation; the error state clears card fields; keyboard focus returns to the page heading after the error.
- Testing not supplied: production analytics, assistive-technology testing, backend idempotency behavior, localized content, and small-screen browser captures.

## Output excerpt

### Audit frame

`Release-risk audit | Responsive web prototype | Cart review -> confirmation | Desktop recording supplied | Overall confidence: moderate`

The prototype supports guest checkout and keeps the order summary visible, but payment feedback and recovery create avoidable transaction risk. Accessibility conformance cannot be determined from the supplied artifacts.

### Critical journey

| Step | User goal | Observed friction | Consequence | Severity |
|---|---|---|---|---|
| Review total | Verify the amount before paying | Delivery changes the total without a change announcement | A user may authorize an amount they did not notice | S2 |
| Submit payment | Know the action was received | Pay remains enabled while processing is silent | Repeat submission and duplicate-charge anxiety | S1 |
| Recover from failure | Correct only the failed input | All card fields clear and focus leaves the payment region | Rework and uncertain recovery | S2 |

#### S1 | High confidence | Payment submission

**Users can submit payment again while the first request appears inactive.**

**Evidence:** In the supplied recording, Pay remains enabled and visually unchanged for four seconds after activation. No progress message appears in the payment region.

**Impact:** A user may repeat the action, increasing duplicate-payment risk if the backend is not idempotent and creating serious anxiety even when it is.

**Root cause:** The interface has no immediate pending state or repeat-submission guard.

**Recommendation:** Enter a pending state immediately, prevent another activation, retain the submitted values, and show a status adjacent to the action. Confirm backend idempotency with engineering rather than implying the interface alone prevents duplicate charges.

**Acceptance criteria:** After activation, the control cannot submit another request while the first is pending; visual and programmatic status identifies payment processing; a timeout exposes a safe recovery path; inputs remain available after a recoverable failure; backend duplicate-request behavior is documented and tested.

#### S2 | High confidence | Total confirmation

**A delivery change can alter the payable amount without drawing attention to the new commitment.**

**Evidence:** Selecting Express updates the final total, but only the number changes. The payment control remains in the same position and no change message is presented.

**Impact:** Rohan may miss the revised amount before authorization, weakening price transparency and trust.

**Root cause:** Delivery selection and payment commitment are visually connected but behaviorally independent.

**Recommendation:** Keep the revised total in the payment decision region and announce the change. Do not add a second confirmation step unless validation shows users still miss the amount.

**Acceptance criteria:** The final amount visible next to Pay always matches the selected delivery method; its update is programmatically announced without moving focus; automated tests verify the amount and delivery method remain synchronized.

### Accessibility

- **Confirmed from keyboard recording:** after the payment error, focus moves to the page heading rather than the error or first invalid field. Verify focus recovery against the implemented semantics.
- **Needs verification:** accessible names, error associations, live-region behavior, contrast, zoom/reflow, and target size were not testable from the supplied recording.
- **No conformance claim:** this artifact review is not a WCAG audit of the production implementation.

### Action plan

- **Now:** prevent repeat submission; define backend duplicate-request behavior; preserve payment data on recoverable failure.
- **Next:** connect delivery changes to the final-payment decision and repair error focus behavior.
- **Later:** validate comprehension and recovery with representative users and realistic latency.

### Preserve

- Guest checkout is available without account interruption.
- The order summary remains visible through the payment step.

### Needs verification

| Question | Evidence needed |
|---|---|
| Can duplicate requests create separate charges? | Payment-service and idempotency tests |
| Do users notice delivery-driven total changes? | Task test using realistic shipping choices |
| Does recovery work with screen readers? | Implemented build tested with supported browser and assistive technology pairs |
