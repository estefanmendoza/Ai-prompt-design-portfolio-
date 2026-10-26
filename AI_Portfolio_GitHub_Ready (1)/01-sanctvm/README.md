# SANCTVM — translating a brand vision into better AI prompts

**Type:** Real AI-assisted ecommerce website project · **Tools:** Base44 and general-purpose AI assistants · **Status:** Prototype/ongoing work

## Challenge

I wanted a fashion-led shopping experience that felt distinctive, intentional and credible—not another generic storefront. A broad first instruction produced an actual website, but the result didn't deliver the premium visual identity or the full customer experience I was asking for.

## What was broken in the first version?

The first result was functional enough to view, but its visual direction felt generic: insufficiently specific hierarchy, composition, product presentation and brand voice. Broad requests left too many decisions to the generator. Subsequent changes could also produce a new inconsistency somewhere else in the site, making each iteration a tradeoff between speed, credits and careful review.

## How I found out

I inspected the rendered/live site rather than trusting the AI's summary of the work. I compared what was visible and interactive with the actual direction I wanted. Separately, a platform security scan identified more serious issues in generated backend/API logic. For example, an order-creation flow accepted a price supplied by the client. That is not a cosmetic problem: pricing must be verified on the server. This finding is documented here as a discovery, **not a claim that I personally implemented and verified the production fix**.

## Example of the prompt revision

The exact original messages are not preserved here; these are **illustrative reconstructions** showing the difference in specificity.

**V1 — broad request**

> Build an ecommerce website for my clothing brand SANCTVM with product pages, a cart, and checkout.

**V2 — measurable creative + functional specification**

> Design SANCTVM as a restrained, dark, editorial ecommerce experience. Use a deliberately sparse navigation, strong type hierarchy and a product-first layout. Avoid default template sections, generic lifestyle stock imagery, and unrequested promotional clutter. Define distinct states for an empty cart, product selection, mobile browsing and checkout. After each change, report exactly which screens and flows changed, what was not implemented, and what needs manual verification. Never treat a visually correct checkout screen as proof of payment security; server-side pricing and authentication require explicit checks.

## Why the second approach is better

- It replaces taste words alone ("premium") with **observable design constraints**.
- It requires **screen/state coverage**, not just an attractive landing page.
- It asks for **change notes and unresolved items**, reducing false confidence.
- It separates **visual success** from verified **backend safety**.

## Review checklist

See [review-checklist.md](review-checklist.md) for the criteria I would apply to future iterations, including product flow and security handoff. These are recommended acceptance criteria, not a claim that every criterion has passed.

## Lessons

A useful prompt should help reveal what was *not* done. I learned to request fewer vague upgrades and more targeted, testable changes. Human observation remains essential: the model's description of a result is not the same as the actual product.
