import DOMPurify from 'isomorphic-dompurify';
import { marked } from 'marked';
import type { Lang } from './threads';

export type Heading = {
	level: number;
	text: string;
	id: string;
};

marked.setOptions({ gfm: true, breaks: false });

export function slugify(text: string): string {
	return text
		.normalize('NFD')
		.replace(/\p{M}/gu, '')
		.toLowerCase()
		.replace(/[^\w\s-]/g, '')
		.replace(/\s+/g, '-')
		.replace(/-+/g, '-')
		.trim();
}

/** Strips the leading H1 and abstract/resumen block from body markdown. */
export function stripFrontMatter(md: string, lang: Lang): string {
	let body = md.replace(/^\s*#\s+.+\n+/, '');
	const label = lang === 'es' ? 'Resumen' : 'Abstract';
	body = body.replace(new RegExp(`^\\*\\*${label}:\\*\\*\\s*.+?(\\n\\n|$)`, 'ms'), '');
	return body.trim();
}

export function extractAbstract(md: string, lang: Lang): string | null {
	const label = lang === 'es' ? 'Resumen' : 'Abstract';
	const match = md.match(new RegExp(`\\*\\*${label}:\\*\\*\\s*(.+?)(?=\\n\\n|$)`, 's'));
	return match?.[1]?.trim() ?? null;
}

export function extractTitle(md: string): string {
	const match = md.match(/^#\s+(.+)$/m);
	return match?.[1]?.trim() ?? 'Untitled';
}

/** Collects ## and ### headings outside fenced code blocks. */
export function buildHeadingToc(md: string): Heading[] {
	const headings: Heading[] = [];
	const seen = new Map<string, number>();
	let inFence = false;

	for (const line of md.split('\n')) {
		if (line.startsWith('```')) {
			inFence = !inFence;
			continue;
		}
		if (inFence) continue;

		const match = line.match(/^(#{2,3})\s+(.+)$/);
		if (!match) continue;

		const level = match[1].length;
		const text = match[2].replace(/\*\*/g, '').trim();
		let id = slugify(text);
		const count = seen.get(id) ?? 0;
		if (count > 0) id = `${id}-${count}`;
		seen.set(slugify(text), count + 1);

		headings.push({ level, text, id });
	}

	return headings;
}

export function renderMarkdown(md: string, headings: Heading[]): string {
	const idQueue = [...headings.map((h) => h.id)];
	const renderer = new marked.Renderer();

	renderer.heading = ({ depth, text }) => {
		const plain = text.replace(/<[^>]+>/g, '');
		const id = depth >= 2 ? (idQueue.shift() ?? slugify(plain)) : '';
		const tag = `h${depth}`;
		return id ? `<${tag} id="${id}">${text}</${tag}>` : `<${tag}>${text}</${tag}>`;
	};

	const raw = marked.parse(md, { renderer }) as string;
	return DOMPurify.sanitize(raw, {
		ADD_ATTR: ['target'],
		ALLOWED_TAGS: [
			'h1',
			'h2',
			'h3',
			'h4',
			'p',
			'a',
			'ul',
			'ol',
			'li',
			'strong',
			'em',
			'code',
			'pre',
			'blockquote',
			'table',
			'thead',
			'tbody',
			'tr',
			'th',
			'td',
			'hr',
			'br'
		]
	});
}
