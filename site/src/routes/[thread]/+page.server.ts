import { error } from '@sveltejs/kit';
import { loadParentAbstract, loadThreadHub, loadThreadNav } from '$lib/content';
import { getThread, threads } from '$lib/threads';

export function entries() {
	return threads.map((t) => ({ thread: t.slug }));
}

export function load({ params }) {
	const thread = getThread(params.thread);
	if (!thread) error(404, 'Thread not found');

	const document = loadThreadHub(params.thread, 'en');
	if (!document) error(404, 'Document not found');

	return {
		thread,
		document,
		parentAbstract: loadParentAbstract(thread, 'en'),
		navItems: loadThreadNav(thread, 'en'),
		activeDoc: thread.parentDocSlug,
		lang: 'en' as const,
		isParentHub: true
	};
}
