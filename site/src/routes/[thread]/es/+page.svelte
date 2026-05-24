<script lang="ts">
	import ThreadDocumentPage from '$lib/components/ThreadDocumentPage.svelte';

	let { data } = $props();
</script>

<ThreadDocumentPage {...data} />
