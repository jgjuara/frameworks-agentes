<script lang="ts">
	import '../app.css';
	import { base } from '$app/paths';
	import PeripheralStimuli from '$lib/components/PeripheralStimuli.svelte';

	let { children } = $props();
</script>

<PeripheralStimuli />

<header class="site-header">
	<a href="{base}/">Codex Frameworks</a>
</header>

{@render children()}
