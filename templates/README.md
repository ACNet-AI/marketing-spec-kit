# Templates Directory

marketing-spec-kit provides a single command layer for marketing execution.

---

## 📂 Directory Structure

```
templates/
└── sdm/                    # Spec-Driven Marketing
    ├── commands/           # 10 SDM commands + README
    └── templates/          # (Deprecated - no longer used)
```

---

## 🚀 SDM Layer (Spec-Driven Marketing)

### Purpose
Execute marketing activities through specification-driven development and code generation.

### Commands (10)

| Command | Category | Purpose |
|---------|----------|---------|
| `/marketspec.constitution` | Core Flow | Define marketing principles |
| `/marketspec.specify` | Core Flow | Define marketing requirements |
| `/marketspec.clarify` | Core Flow | Clarify objectives and resolve ambiguities |
| `/marketspec.plan` | Core Flow | Plan marketing strategy |
| `/marketspec.checklist` | Core Flow | Generate quality standards |
| `/marketspec.tasks` | Core Flow | Generate implementation tasks |
| `/marketspec.analyze` | Core Flow | Check consistency & coverage |
| `/marketspec.implement` | Core Flow | Generate code + configs ⭐ |
| `/marketspec.review` | Extension | Analyze campaign results |
| `/marketspec.optimize` | Extension | Generate optimization recommendations |

**Status**: ✅ Commands fully implemented (v0.4.0)

### Quick Start Example

```bash
# Complete workflow
/marketspec.specify "Q1 Growth Campaign"
/marketspec.plan
/marketspec.tasks
/marketspec.implement
→ Output: src/campaigns/001-q1.ts + config/001-q1.yaml + templates/001-q1/
```

---

## 🔧 Advanced: Extending MCP Tools

### When do you need to extend?

The default implementation generates code for common tools like GitHub, Twitter, Analytics.

If you need domain-specific tools (e.g., Shopify for e-commerce, HubSpot for B2B), you can extend.

### How to extend?

**Define custom MCP tool wrappers** in `src/shared/mcp-tools/`:

```typescript
// src/shared/mcp-tools/shopify.ts
export async function getOrders(params: { since: string }) {
  const client = await getMCPClient('shopify');
  return await client.call('get_orders', params);
}

export async function trackAbandonedCarts() {
  // Implementation
}
```

### Extension Examples

#### E-commerce Extension
Custom tools: `shopify.ts`, `stripe.ts`, `klaviyo.ts`

```typescript
// Track flash sale performance
const sales = await shopify.getOrders({ 
  since: campaign.start_date 
});
```

#### B2B Extension
Custom tools: `hubspot.ts`, `salesforce.ts`, `linkedin.ts`

```typescript
// Track lead engagement
const leads = await hubspot.getLeads({ 
  score: { min: 80 } 
});
```

#### SaaS Extension
Custom tools: `mixpanel.ts`, `segment.ts`, `intercom.ts`

```typescript
// Track trial conversions
const conversions = await mixpanel.getConversions({ 
  event: 'trial_to_paid' 
});
```

---

## 📚 Learn More

- [SDM Commands Guide](./sdm/README.md)
- [Domain Specification](../specs/domain/001-marketing-operations-spec/spec.md)
- [MetaSpec SDS Documentation](../.metaspec/README.md)
- [Architecture Decisions](../docs/internal/architecture-decisions-2025-11-16.md)
