<script lang="ts">
	import { base } from '$app/paths';

	let {
		threadSlug,
		items,
		activeDoc,
		parentDocSlug,
		lang
	}: {
		threadSlug: string;
		items: { slug: string; title: string }[];
		activeDoc: string;
		parentDocSlug: string;
		lang: 'en' | 'es';
	} = $props();

	function docHref(slug: string): string {
		const root = lang === 'es' ? `${base}/${threadSlug}/es` : `${base}/${threadSlug}`;
		return slug === parentDocSlug ? root : `${root}/${slug}`;
	}
</script>

<nav class="thread-toc" aria-label="Thread documents">
	<p class="thread-toc__title">{lang === 'es' ? 'Documentos' : 'Documents'}</p>
	<ul>
		{#each items as item}
			<li>
				<a href={docHref(item.slug)} aria-current={item.slug === activeDoc ? 'page' : undefined}>
					{item.title}
				</a>
			</li>
		{/each}
	</ul>
</nav>
