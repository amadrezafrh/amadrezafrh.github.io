# Experience Section Guidelines

## Structure

Each experience entry follows this HTML structure:

```html
<article class="experience-item">
  <div class="experience-header">
    <h3>{Job Title}</h3>
    <span class="experience-date">{Start Date} - {End Date}</span>
  </div>
  <div class="experience-company-row">
    <span class="experience-company">{Company Name}</span>
    <span class="experience-location">{City}</span>
  </div>
  <ul>
    <li>{Bullet point}</li>
  </ul>
</article>
```

## Layout Rules

- **Header row**: Job title (left) and date range (right)
- **Company row**: Company name (left) and location/city (right)
- **Bullets**: Listed below company row

## Bullet Point Guidelines

Each bullet should demonstrate professional impact using this structure:

```
[Action Verb] + [What You Built/Did] + [Technologies Used] + [Quantifiable Result/Impact]
```

### Action Verbs (Strong, Past Tense)
- Designed, Architectured, Developed, Built, Engineered
- Supervised, Led, Mentored, Orchestrated
- Shipped, Deployed, Delivered, Automated
- Reduced, Improved, Raised, Optimized

### Technology Mentions
- Include in parentheses: `(Python, PyTorch, Docker)`
- Be specific: `YOLOv8` not just `YOLO`
- Group related: `(Docker + Kubernetes, SageMaker)`

### Quantifiable Results
- Use metrics: `~30%`, `10%`, `~50 hours per month`
- Compare to baselines: `compared to open source baselines`
- Show business impact: `reducing manual review effort`, `productized for external clients`

## Examples

Good:
```
Developed an aquatic-vegetation detection pipeline (Docker + Kubernetes, SageMaker) using multispectral satellite data, with Prometheus observability, reducing human inspection by 80% and compute cost by 35% while maintaining less than 3% accuracy drift
```

Structure breakdown:
- Action: Developed
- What: aquatic-vegetation detection pipeline
- Tech: (Docker + Kubernetes, SageMaker), multispectral satellite data, Prometheus
- Impact: reducing human inspection by 80%, compute cost by 35%, <3% accuracy drift

## Date Format

- Use: `Mon YYYY - Mon YYYY` or `Mon YYYY - Present`
- Examples: `Nov 2024 - Present`, `Aug 2023 - Nov 2024`

## Location Format

- City name only: `Turin`, `Darmstadt`, `Tehran`
- No country needed

## Content Rules

- Match CV exactly - no paraphrasing
- No emojis
- Keep technical accuracy
- Each bullet should stand alone as proof of capability
