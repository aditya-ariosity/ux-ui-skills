# Governance and Adoption

## Contents

- System as a product
- Decision rights
- Contribution workflow
- Release, versioning, and deprecation
- Exceptions and extensions
- Adoption and health measures
- Migration planning
- Source discipline

## System as a product

Define:

- consumers and the jobs the system must improve;
- product/platform scope and explicit non-goals;
- core team, contributors, sponsors, and support model;
- service expectations for review, releases, defects, and accessibility;
- roadmap inputs and prioritization criteria;
- funding and maintenance responsibility.

Do not judge health by component count. Judge whether teams can find, trust, adopt, extend, and update shared decisions without degrading product outcomes.

## Decision rights

Assign an accountable role for:

- foundations and tokens;
- component behavior and APIs;
- accessibility and inclusive defaults;
- content standards;
- design assets and code packages;
- contribution acceptance;
- versioning and releases;
- product exceptions;
- migration and support;
- measurement and roadmap.

Use consultation broadly but make final decision rights explicit. A committee with no accountable owner creates delay and unofficial forks.

## Contribution workflow

Use a visible lifecycle:

`Need -> evidence -> existing-pattern check -> proposal -> design/technical/accessibility review -> build -> test -> pilot -> document -> release -> measure`

A proposal should include:

- user and product need with real instances;
- why composition or an existing variant is insufficient;
- intended scope and consumers;
- behavior, content, state, responsive, and accessibility contract;
- API and token implications;
- alternatives and tradeoffs;
- test evidence;
- ownership and maintenance plan;
- migration or adoption path.

Let product teams contribute without transferring permanent maintenance silently. Define review service levels so urgent work does not bypass the system by necessity.

## Release, versioning, and deprecation

Classify changes by consumer impact, not team intent:

- visual-compatible fix;
- behavioral fix;
- additive token, property, variant, or component;
- deprecated contract;
- breaking rename, removal, default change, semantic change, or interaction change.

For every release provide:

- version and status;
- affected packages, assets, and platforms;
- design and code availability;
- change rationale;
- before/after behavior;
- migration instructions or codemod where feasible;
- accessibility and test notes;
- deprecation date and support window;
- known limitations.

Do not deprecate without a replacement or explicit exit path. Do not keep deprecated contracts indefinitely without measuring remaining consumers.

## Exceptions and extensions

Create an exception record:

`Product need | Existing limitation | Scope | Owner | Accessibility review | Expiry or revisit | Upstream candidate`

Legitimate exceptions may arise from platform conventions, expert workflows, regulatory needs, brand differentiation, performance, or unique data. Distinguish these from accidental drift.

Provide safe extension mechanisms: slots, composition, recipes, semantic token hooks, or documented product-level patterns. Avoid unrestricted styling hooks that break states and accessibility.

## Adoption and health measures

Combine quantitative and qualitative evidence:

- percentage of eligible product instances using supported components;
- version distribution and deprecated usage;
- token bypasses and duplicate implementations;
- design-code parity gaps;
- accessibility defects and escape frequency;
- time to discover, implement, and upgrade;
- contribution lead time and rejection reasons;
- support volume and recurring confusion;
- consumer confidence and task success;
- product quality or delivery outcomes tied to system changes.

Do not use a single adoption percentage as the health score. A widely used inaccessible component is not success.

## Migration planning

1. Inventory consumers and dependencies.
2. Classify by risk, effort, product lifecycle, and owner.
3. Stabilize the replacement and documentation.
4. Pilot in representative products and platforms.
5. Provide mapping, examples, tests, and tooling.
6. Sequence shared foundations before dependent components.
7. Track exceptions and blocked teams.
8. Verify behavior and accessibility in product context.
9. Remove deprecated paths only after evidence and communication support it.

Prefer a migration that creates visible product or delivery benefit. Cleanup with no consumer value loses priority and encourages forks.

## Source discipline

Research snapshot: 2026-08-09.

Useful public precedents include [GOV.UK Design System](https://design-system.service.gov.uk/), [USWDS](https://designsystem.digital.gov/), [Material Design 3](https://m3.material.io/), [Apple HIG](https://developer.apple.com/design/human-interface-guidelines/), [Carbon](https://carbondesignsystem.com/), [Adobe Spectrum](https://spectrum.adobe.com/), [Atlassian Design](https://atlassian.design/), [Fluent 2](https://fluent2.microsoft.design/), and [Shopify Polaris](https://polaris.shopify.com/).

Treat each as evidence of one organization's decisions, constraints, and operating model. Do not merge their token values, component behaviors, or governance rules into a synthetic universal system. `Design Systems` by Alla Kholmatova is a useful operating-model foundation; pair it with current system documentation and product evidence.
