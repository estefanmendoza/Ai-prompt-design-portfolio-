# ESTEFAN OS — CRM & campaign workflow design

**Project:** Estefan CRM / Command Center (ESTEFAN OS)  
**Role:** Independent builder, product and workflow design through AI-assisted development  
**Platform:** Base44  
**Status:** Unpublished, in development; interface demonstrated with an actual in-app screenshot

![SMS Campaigns screen, cropped before contact records](assets/sms-campaign-flow.png)

## Overview

I built a sales-oriented CRM interface with an AI-assisted application builder to bring lead information, pipeline activity, outreach, and reporting into one workspace. The screenshot documents one part of that work: a staged SMS campaign composer with an audience-selection screen.

My background in full-cycle sales shaped the product decisions. I wanted campaign setup to be explicit and reviewable, rather than a single uncontrolled **send** action.

## What is visible in the app

The captured interface contains:

- A navigation structure for **Dashboard, Leads, Deals, Data, Marketing, SMS & Calling, Broadcasts, SMS Campaigns, Opened Messages, Analytics, Agent Performance, and Integrations**.
- A five-step **SMS campaign journey**: **Audience → Message → Preview → Confirm → Results**.
- Audience filters covering **CRM stage, city, state, property type, offer range, and text search**.
- Separate UI categories for **filtered, eligible, opted-out, and missing-phone** records.
- A dedicated review/confirmation step in the displayed flow before the results step.

The visible record counts are **snapshot UI values**, not claims of delivered messages, authenticated consent, production traffic, or successful campaign outcomes.

## Design problem

In outreach tools, combining audience selection, personalization and sending into one opaque action makes errors hard to spot. The interface separates these decisions into a sequence that can be reviewed. An operator should know **who** is in scope, **what** message will be sent, and **whether** the campaign is ready before any sending operation.

### Intent of the flow

```text
Select audience -> Write message -> Preview personalized outputs
                -> Explicit confirmation -> Results / feedback
```

This is **workflow and UI design evidence**. I have not supplied evidence here that external SMS sending, carrier integrations, consent verification, delivery tracking, or all screens in the flow have been tested end to end.

## Prompt design approach

The work involved translating sales-operations requirements into prompts for an AI-assisted application builder and reviewing the generated product in the application itself.

The following is a **representative design specification**, written for this portfolio to explain the intended workflow. It is **not** presented as a verbatim historical Base44 prompt:

> Design a five-stage SMS campaign interface for CRM contacts: Audience, Message, Preview, Confirm and Results. Require an explicit audience selection before drafting. Show separate states for contacts lacking a phone number, contacts with a verified opt-out, and contacts whose consent status has not been verified. Personalization should be previewable for individual contacts, including missing-field fallbacks. Never describe a contact as legally eligible solely because a phone number exists. Nothing should be sent without an affirmative user confirmation. Surface failed sends and retries separately from confirmed results. State clearly which behaviors depend on a real provider integration.

**Why this matters:** The prompt translates a vague instruction such as "add SMS marketing" into interaction states, safety boundaries, and expected behavior that can be inspected.

## Evaluation scenarios to run next

These are **proposed checks**, not reported test results:

| Scenario | Expected result |
| --- | --- |
| A contact has no phone number | Excluded from sendable audience; reason displayed |
| A contact has opted out | Not selectable for marketing send |
| Contact consent is unknown | Not silently treated as permission to send |
| Personalization field is missing | Preview gives an explicit, safe fallback |
| Operator changes the audience after preview | Previous preview/confirmation becomes invalid |
| Operator cancels at confirmation | No message is sent |
| Provider fails or times out | Actual send status remains unknown/failed, not 'delivered' |
| User retries after timeout | Avoid duplicate delivery; explain status uncertainty |

## What I learned and what I'd improve

A useful AI-generated interface is not enough: the critical work is turning it into a reliable experience with correct permission handling, explicit actions, error states and verifiable outcomes. The visual flow is a starting point, not proof of a compliant messaging system.

Before any real campaign use, I'd require a verified consent model, applicable SMS compliance review (including TCPA and provider policies), server-side authorization, opt-out enforcement, delivery logs, rate limiting, and integration tests. The screenshot alone establishes **none** of those safeguards.

## Relevance to conversational AI

This project demonstrates the way I think about **multi-step interaction design**: break actions into coherent turns, preserve the user's goal across steps, expose state clearly, and prevent surprising irreversible actions. Those ideas also matter when writing prompts for conversational agents, especially in sensitive settings.

**Project status:** Independently developed Base44 application, currently in development. The screenshots illustrate the interface and workflow design.
