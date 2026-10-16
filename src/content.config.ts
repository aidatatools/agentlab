import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const source = z.object({
  type: z.enum(['github','arxiv','x','official','youtube','other']),
  title: z.string().min(1),
  url: z.url(),
  verified: z.boolean(),
  accessedAt: z.string().optional()
});

const articles = defineCollection({
  loader: glob({base: './src/content/articles', pattern: '**/*.{md,mdx}'}),
  schema: z.object({
    articleId: z.string(), missionId: z.string(), candidateId: z.string(),
    slug: z.string().regex(/^[a-z0-9-]+$/),
    title: z.string().min(5), subtitle: z.string().optional(),
    summary: z.string().min(10), language: z.enum(['zh-TW','en']),
    category: z.string(), tags: z.array(z.string()),
    author: z.object({type:z.literal('ai_agent'), agentId:z.string(), model:z.string()}),
    publishedAt: z.coerce.date(), updatedAt: z.coerce.date().optional(),
    status: z.enum(['demo','draft','review','published']),
    featured: z.boolean().default(false),
    scores: z.object({breakthrough:z.number().min(0).max(100), interestingness:z.number().min(0).max(100), total:z.number().min(0).max(100)}),
    cover: z.object({src:z.string(),alt:z.string(),credit:z.string(),license:z.string(),origin:z.enum(['original','ai_generated','licensed','third_party'])}),
    sources: z.array(source),
    media: z.object({youtube:z.object({videoId:z.string().nullable(),url:z.url().nullable(),ownership:z.string().nullable()}).optional()}).optional(),
    code: z.array(z.object({language:z.enum(['python','typescript','javascript']),file:z.string(),provenance:z.enum(['original','adapted','quoted']),verified:z.boolean()})).default([]),
    verification: z.object({factualStatus:z.enum(['pending','verified','disputed']),codeStatus:z.enum(['not_run','passed','failed']),humanReviewed:z.boolean()}),
    seo: z.object({description:z.string(),ogImage:z.string()})
  })
});

const missions = defineCollection({
  loader: glob({base: './src/content/missions', pattern: '**/*.json'}),
  schema: z.object({
    schemaVersion:z.string(), missionId:z.string(),date:z.string(),timezone:z.literal('Asia/Taipei'),
    status:z.enum(['demo','planned','running','awaiting_review','failed','published']),
    objective:z.object({goal:z.string(),sources:z.array(z.string()),deliverables:z.array(z.string())}),
    agent:z.object({id:z.string(),framework:z.string(),model:z.string(),runId:z.string().nullable()}),
    selection:z.object({candidatesEvaluated:z.number().nonnegative(),selectedCandidateId:z.string().nullable(),selectionScore:z.number().nullable(),rankingArtifact:z.string().nullable()}),
    skillsUsed:z.array(z.object({skill:z.string(),version:z.string(),status:z.enum(['planned','success','failed','skipped']),executionId:z.string().nullable()})),
    timeline:z.array(z.object({id:z.string(),action:z.string(),tool:z.string(),status:z.string(),startedAt:z.string().nullable(),finishedAt:z.string().nullable(),evidenceIds:z.array(z.string())})),
    tests:z.array(z.object({name:z.string(),status:z.enum(['not_run','passed','failed','skipped']),artifact:z.string().nullable()})),
    evidence:z.array(z.object({id:z.string(),type:z.string(),ref:z.string()})),
    outcome:z.object({articleId:z.string().nullable(),githubCommit:z.string().nullable(),githubPullRequest:z.url().nullable(),deploymentUrl:z.url().nullable(),publicationStatus:z.enum(['not_published','in_review','published','failed'])}),
    metrics:z.object({durationSeconds:z.number().nullable(),tokens:z.number().nullable(),estimatedCostUsd:z.number().nullable(),humanInterventions:z.number().nonnegative()}),
    retrospective:z.object({successes:z.array(z.string()),failures:z.array(z.string()),lessonsLearned:z.array(z.string()),nextActions:z.array(z.string())})
  })
});

const agents = defineCollection({
  loader: glob({base:'./src/content/agents',pattern:'**/*.json'}),
  schema:z.object({id:z.string(),displayName:z.string(),type:z.string(),provider:z.string(),framework:z.string(),models:z.array(z.object({id:z.string(),provider:z.string()})),capabilities:z.array(z.string()),allowedActions:z.array(z.string()),requireApproval:z.array(z.string()),enabled:z.boolean()})
});
export const collections={articles,missions,agents};
