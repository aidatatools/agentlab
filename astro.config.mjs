import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';

export default defineConfig({
  site: 'https://agentlab.aidatatools.com',
  output: 'static',
  integrations: [mdx()],
  trailingSlash: 'always'
});
