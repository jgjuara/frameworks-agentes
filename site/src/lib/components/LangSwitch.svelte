<script lang="ts">
	import { base } from '$app/paths';

	let {
		threadSlug,
		docSlug,
		lang,
		isParentHub = false
	}: {
		threadSlug: string;
		docSlug: string;
		lang: 'en' | 'es';
		isParentHub?: boolean;
	} = $props();

	function href(targetLang: 'en' | 'es'): string {
		const enRoot = `${base}/${threadSlug}`;
		const esRoot = `${base}/${threadSlug}/es`;

		if (isParentHub) {
			return targetLang === 'es' ? esRoot : enRoot;
		}

		return targetLang === 'es' ? `${esRoot}/${docSlug}` : `${enRoot}/${docSlug}`;
	}
</script>

<div class="lang-switch" role="navigation" aria-label="Language">
	<a href={href('en')} aria-current={lang === 'en' ? 'true' : undefined}>English</a>
	<span aria-hidden="true">·</span>
	<a href={href('es')} aria-current={lang === 'es' ? 'true' : undefined}>Español</a>
</div>
