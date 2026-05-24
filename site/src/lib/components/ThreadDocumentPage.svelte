<script lang="ts">
	import { base } from '$app/paths';
	import EmptyTranslation from './EmptyTranslation.svelte';
	import LangSwitch from './LangSwitch.svelte';
	import MarkdownBody from './MarkdownBody.svelte';
	import ParentAbstract from './ParentAbstract.svelte';
	import ThreadToc from './ThreadToc.svelte';
	import type { LoadedDocument } from '$lib/content';
	import type { Lang, Thread } from '$lib/threads';

	let {
		thread,
		document,
		parentAbstract,
		navItems,
		activeDoc,
		lang,
		isParentHub = false
	}: {
		thread: Thread;
		document: LoadedDocument;
		parentAbstract: string | null;
		navItems: { slug: string; title: string }[];
		activeDoc: string;
		lang: Lang;
		isParentHub?: boolean;
	} = $props();

</script>

<svelte:head>
	<title
		>{document.title} · {lang === 'es' ? thread.titleEs : thread.titleEn}</title
	>
</svelte:head>

<div class="page-shell">
	<aside class="thread-sidebar">
		<ThreadToc
			threadSlug={thread.slug}
			items={navItems}
			{activeDoc}
			parentDocSlug={thread.parentDocSlug}
			{lang}
		/>
	</aside>

	<main class="main-column">
		<LangSwitch threadSlug={thread.slug} docSlug={activeDoc} {lang} {isParentHub} />

		<p class="thread-breadcrumb">
			<a href="{base}/">{lang === 'es' ? 'Inicio' : 'Home'}</a>
			<span aria-hidden="true"> / </span>
			<span>{lang === 'es' ? thread.titleEs : thread.titleEn}</span>
		</p>

		{#if parentAbstract}
			<ParentAbstract
				text={parentAbstract}
				label={lang === 'es' ? 'Resumen del informe' : 'Report abstract'}
			/>
		{/if}

		{#if document.hasContent}
			<MarkdownBody html={document.bodyHtml} />
		{:else}
			<EmptyTranslation />
		{/if}
	</main>
</div>

<style>
	.thread-breadcrumb {
		margin: 0 0 1.25rem;
		font-size: 0.85rem;
		color: var(--text-muted);
	}

	.thread-breadcrumb a {
		color: var(--text-muted);
		text-decoration: none;
	}

	.thread-breadcrumb a:hover {
		color: var(--text);
	}
</style>
