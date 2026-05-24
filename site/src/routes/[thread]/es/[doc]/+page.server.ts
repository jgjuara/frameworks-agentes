import { error } from '@sveltejs/kit';
import { loadDocument, loadParentAbstract, loadThreadNav } from '$lib/content';
import { getThread, threads } from '$lib/threads';

export function entries() {
	return threads.flatMap((t) =>
		t.docs
			.filter((d) => d.slug !== t.parentDocSlug)
			.map((d) => ({ thread: t.slug, doc: d.slug }))
	);
}

export function load({ params }) {
	const thread = getThread(params.thread);
	if (!thread) error(404, 'Thread not found');

	const document = loadDocument(params.thread, params.doc, 'es');
	if (!document) error(404, 'Document not found');

	return {
		thread,
		document,
		parentAbstract: loadParentAbstract(thread, 'es'),
		navItems: loadThreadNav(thread, 'es'),
		activeDoc: params.doc,
		lang: 'es' as const,
		isParentHub: false
	};
}
