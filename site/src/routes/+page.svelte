<script lang="ts">
	import { base } from '$app/paths';
	import ParentAbstract from '$lib/components/ParentAbstract.svelte';

	let { data } = $props();
</script>

<svelte:head>
	<title>Codex Frameworks</title>
</svelte:head>

<div class="page-shell page-shell--home">
	<main class="main-column">
		<h1>Codex Frameworks</h1>
		<p class="home-intro">
			Research-team guidance on context, prompting, and agentic workflows for Codex.
		</p>

		<ul class="home-list">
			{#each data.cards as card}
				<li>
					<h2><a href="{base}/{card.slug}">{card.title}</a></h2>
					{#if card.abstract}
						<ParentAbstract text={card.abstract} />
					{/if}
				</li>
			{/each}
		</ul>
	</main>
</div>

<style>
	h1 {
		margin: 0 0 0.75rem;
		font-size: 1.75rem;
		font-weight: 600;
	}

	.home-intro {
		margin: 0 0 2.5rem;
		color: var(--text-muted);
	}
</style>
