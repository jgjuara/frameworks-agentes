<script lang="ts">
	let { text, label = 'Abstract' }: { text: string; label?: string } = $props();
</script>

<aside class="parent-abstract">
	<span class="parent-abstract__label">{label}</span>
	{text}
</aside>
