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
// Skills count as used only when a real (non-demo) mission records a successful execution.
export async function getVerifiedSkillUse() {
  const missions=(await getMissions()).filter(m=>m.data.status!=='demo');
  const use=new Map<string,{agentId:string,missionId:string,date:string}[]>();
  for (const m of missions) for (const s of m.data.skillsUsed) {
    if (s.status!=='success') continue;
    use.set(s.skill,[...(use.get(s.skill)??[]),{agentId:m.data.agent.id,missionId:m.data.missionId,date:m.data.date}]);
  }
  return use;
}
export function articleUrl(slug:string) {return `/discoveries/${slug}/`;}
export function missionUrl(missionId:string){return `/missions/${missionId}/`;}
