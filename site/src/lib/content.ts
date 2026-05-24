import { readFileSync, existsSync } from 'node:fs';
import { join } from 'node:path';
import {
	buildHeadingToc,
	extractAbstract,
	extractTitle,
	renderMarkdown,
	stripFrontMatter
} from './markdown';
import {
	getThread,
	getThreadDoc,
	threads,
	type Lang,
	type Thread,
	type ThreadDoc
} from './threads';

/** Resolved from site/ working directory during dev and production build. */
const strategyDir = join(process.cwd(), '..', 'strategy');

function resolvePath(lang: Lang, filename: string): string {
	return lang === 'es' ? join(strategyDir, 'es', filename) : join(strategyDir, filename);
}

function readMarkdown(lang: Lang, filename: string): string | null {
	const path = resolvePath(lang, filename);
	if (!existsSync(path)) return null;
	const raw = readFileSync(path, 'utf-8').trim();
	return raw.length > 0 ? raw : null;
}

export type LoadedDocument = {
	title: string;
	abstract: string | null;
	bodyHtml: string;
	hasContent: boolean;
};

export function loadParentAbstract(thread: Thread, lang: Lang): string | null {
	const filename = lang === 'es' ? thread.parentEsFile : thread.parentEnFile;
	const md = readMarkdown(lang, filename);
	if (!md) return null;
	return extractAbstract(md, lang);
}

export function loadDocument(
	threadSlug: string,
	docSlug: string,
	lang: Lang
): LoadedDocument | null {
	const thread = getThread(threadSlug);
	if (!thread) return null;

	const doc = getThreadDoc(thread, docSlug);
	if (!doc) return null;

	const filename = lang === 'es' ? doc.esFile : doc.enFile;
	const md = readMarkdown(lang, filename);

	if (!md) {
		return {
			title: docSlug,
			abstract: null,
			bodyHtml: '',
			hasContent: false
		};
	}

	const headings = buildHeadingToc(md);
	const body = stripFrontMatter(md, lang);

	return {
		title: extractTitle(md),
		abstract: extractAbstract(md, lang),
		bodyHtml: renderMarkdown(body, headings),
		hasContent: true
	};
}

export function loadThreadHub(threadSlug: string, lang: Lang): LoadedDocument | null {
	const thread = getThread(threadSlug);
	if (!thread) return null;
	return loadDocument(threadSlug, thread.parentDocSlug, lang);
}

export type HomeThreadCard = {
	slug: string;
	title: string;
	abstract: string | null;
};

export function loadHomeCards(lang: Lang = 'en'): HomeThreadCard[] {
	return threads.map((thread) => {
		const filename = lang === 'es' ? thread.parentEsFile : thread.parentEnFile;
		const md = readMarkdown(lang, filename);
		const title = md ? extractTitle(md) : lang === 'es' ? thread.titleEs : thread.titleEn;
		return {
			slug: thread.slug,
			title,
			abstract: md ? extractAbstract(md, lang) : null
		};
	});
}

export type ThreadNavItem = {
	slug: string;
	title: string;
};

export function loadThreadNav(thread: Thread, lang: Lang): ThreadNavItem[] {
	return thread.docs.map((doc) => {
		const filename = lang === 'es' ? doc.esFile : doc.enFile;
		const md = readMarkdown(lang, filename);
		return {
			slug: doc.slug,
			title: md ? extractTitle(md) : doc.slug
		};
	});
}

export { getThread, getThreadDoc };
export type { Thread, ThreadDoc, Lang };
