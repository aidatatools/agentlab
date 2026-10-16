// Example-only TypeScript scoring function. Not a claim that any source is verified.
export type Scores = { breakthrough: number; interestingness: number; technicalDepth: number; reproducibility: number; credibility: number };
export function rank(scores: Scores): number {
  const weights: Scores = {breakthrough:.30,interestingness:.25,technicalDepth:.20,reproducibility:.15,credibility:.10};
  return Number((Object.entries(weights).reduce((sum,[key,weight]) => sum + scores[key as keyof Scores]*weight,0)).toFixed(2));
}
