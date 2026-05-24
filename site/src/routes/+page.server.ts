import { loadHomeCards } from '$lib/content';

export function load() {
	return {
		cards: loadHomeCards('en')
	};
}
