<script lang="ts">
	let { html }: { html: string } = $props();
</script>

<article class="markdown-body">
	{@html html}
</article>
