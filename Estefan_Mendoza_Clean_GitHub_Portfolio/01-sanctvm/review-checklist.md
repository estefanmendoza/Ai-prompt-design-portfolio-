# SANCTVM / iteration review checklist

These are **review targets**, not a passed security audit.

## Visual consistency
- [ ] Typography, spacing and image style remain consistent on home, collection, product and cart screens.
- [ ] Product photography and descriptions reflect the actual item, not AI-invented attributes.
- [ ] Mobile navigation and product details remain usable on small screens.
- [ ] No default-template copy or unrequested sections were introduced.

## End-to-end customer flow
- [ ] Product details are accurate, including size and availability.
- [ ] Cart totals and shipping logic are checked against server-side values.
- [ ] Checkout clearly states any blocked or incomplete integration.
- [ ] Successful order confirmation is shown only after verified backend status.

## Trust and security handoff
- [ ] Server independently determines product price; browser-provided price is never trusted.
- [ ] Webhooks are authenticated; a missing secret fails safely rather than bypassing checks.
- [ ] Analytics/event endpoints validate authorization and limit untrusted input where applicable.
- [ ] No secrets or private customer information appear in generated code, logs or prompts.

## Prompt change log template
| Version | Requested change | Observable result | Unexpected regression | Next focused fix |
|---|---|---|---|---|
| vX | (describe) | (link screenshot/test) | (describe or none) | (describe) |
