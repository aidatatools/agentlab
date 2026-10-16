import { getCollection } from 'astro:content';

export async function getPublicArticles() {
  const items = await getCollection('articles', ({ data }) => data.status === 'published');
  return items.sort((a,b) => b.data.publishedAt.getTime() - a.data.publishedAt.getTime());
}
export async function getDemoArticles() {
  return getCollection('articles',({data})=>data.status==='demo');
}
export async function getMissions() {
  const items=await getCollection('missions');
  return items.sort((a,b)=>b.data.date.localeCompare(a.data.date));
}
export function articleUrl(slug:string) {return `/discoveries/${slug}/`;}
export function missionUrl(missionId:string){return `/missions/${missionId}/`;}
