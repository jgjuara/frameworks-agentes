<script lang="ts">
	import type { Heading } from '$lib/markdown';

	let { headings, label = 'On this page' }: { headings: Heading[]; label?: string } = $props();
</script>

{#if headings.length > 0}
	<nav class="doc-toc" aria-label="Document sections">
		<p class="doc-toc__title">{label}</p>
		<ul>
			{#each headings as heading}
				<li data-level={heading.level}>
					<a href="#{heading.id}">{heading.text}</a>
				</li>
			{/each}
		</ul>
	</nav>
{/if}
