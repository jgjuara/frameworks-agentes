import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

const base = process.env.BASE_PATH ?? '';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	preprocess: vitePreprocess(),
	kit: {
		adapter: adapter({
			pages: 'build',
			assets: 'build',
			fallback: undefined,
			precompress: false,
			strict: true
		}),
		paths: {
			base
		},
		prerender: {
			entries: ['*'],
			handleHttpError: ({ path, message }) => {
				if (path.endsWith('.md')) return;
				throw new Error(message);
			},
			handleMissingId: () => {}
		}
	}
};

export default config;
