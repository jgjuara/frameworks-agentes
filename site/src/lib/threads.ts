export type Lang = 'en' | 'es';

export type ThreadDoc = {
	slug: string;
	enFile: string;
	esFile: string;
};

export type Thread = {
	slug: string;
	titleEn: string;
	titleEs: string;
	parentDocSlug: string;
	parentEnFile: string;
	parentEsFile: string;
	docs: ThreadDoc[];
};

export const threads: Thread[] = [
	{
		slug: 'agentic-work',
		titleEn: 'Codex Agentic Work',
		titleEs: 'Trabajo agentic con Codex',
		parentDocSlug: 'report',
		parentEnFile: 'CODEX_AGENTIC_WORK_REPORT.md',
		parentEsFile: 'CODEX_AGENTIC_WORK_REPORT.es.md',
		docs: [
			{
				slug: 'report',
				enFile: 'CODEX_AGENTIC_WORK_REPORT.md',
				esFile: 'CODEX_AGENTIC_WORK_REPORT.es.md'
			},
			{
				slug: 'initial-conditions',
				enFile: 'CODEX_INITIAL_CONDITIONS_FRAMEWORK.md',
				esFile: 'CODEX_INITIAL_CONDITIONS_FRAMEWORK.es.md'
			},
			{
				slug: 'evidence-review',
				enFile: 'CODEX_EVIDENCE_REVIEW.md',
				esFile: 'CODEX_EVIDENCE_REVIEW.es.md'
			},
			{
				slug: 'final-review',
				enFile: 'CODEX_FINAL_REVIEW_PLAYBOOK.md',
				esFile: 'CODEX_FINAL_REVIEW_PLAYBOOK.es.md'
			},
			{
				slug: 'templates',
				enFile: 'CODEX_TEMPLATES.md',
				esFile: 'CODEX_TEMPLATES.es.md'
			}
		]
	},
	{
		slug: 'verifiable-context',
		titleEn: 'Verifiable Codex Context',
		titleEs: 'Contexto verificable para Codex',
		parentDocSlug: 'report',
		parentEnFile: 'CODEX_CONTEXT_PROMPTING_REPORT.md',
		parentEsFile: 'CODEX_CONTEXT_PROMPTING_REPORT.es.md',
		docs: [
			{
				slug: 'report',
				enFile: 'CODEX_CONTEXT_PROMPTING_REPORT.md',
				esFile: 'CODEX_CONTEXT_PROMPTING_REPORT.es.md'
			},
			{
				slug: 'framework',
				enFile: 'CODEX_CONTEXT_PROMPTING_FRAMEWORK.md',
				esFile: 'CODEX_CONTEXT_PROMPTING_FRAMEWORK.es.md'
			},
			{
				slug: 'experiment',
				enFile: 'CODEX_CONTEXT_PROMPTING_EXPERIMENT.md',
				esFile: 'CODEX_CONTEXT_PROMPTING_EXPERIMENT.es.md'
			},
			{
				slug: 'evidence',
				enFile: 'CODEX_CONTEXT_PROMPTING_EVIDENCE.md',
				esFile: 'CODEX_CONTEXT_PROMPTING_EVIDENCE.es.md'
			},
			{
				slug: 'templates',
				enFile: 'CODEX_CONTEXT_PROMPTING_TEMPLATES.md',
				esFile: 'CODEX_CONTEXT_PROMPTING_TEMPLATES.es.md'
			}
		]
	},
	{
		slug: 'non-verifiable-reports',
		titleEn: 'Non-Verifiable Research Reports',
		titleEs: 'Informes de investigación no verificables',
		parentDocSlug: 'main-report',
		parentEnFile: 'CODEX_NON_VERIFIABLE_REPORTS_MAIN_REPORT.md',
		parentEsFile: 'CODEX_NON_VERIFIABLE_REPORTS_MAIN_REPORT.es.md',
		docs: [
			{
				slug: 'main-report',
				enFile: 'CODEX_NON_VERIFIABLE_REPORTS_MAIN_REPORT.md',
				esFile: 'CODEX_NON_VERIFIABLE_REPORTS_MAIN_REPORT.es.md'
			},
			{
				slug: 'operating-framework',
				enFile: 'CODEX_NON_VERIFIABLE_REPORTS_OPERATING_FRAMEWORK.md',
				esFile: 'CODEX_NON_VERIFIABLE_REPORTS_OPERATING_FRAMEWORK.es.md'
			},
			{
				slug: 'experiment-protocol',
				enFile: 'CODEX_NON_VERIFIABLE_REPORTS_EXPERIMENT_PROTOCOL.md',
				esFile: 'CODEX_NON_VERIFIABLE_REPORTS_EXPERIMENT_PROTOCOL.es.md'
			},
			{
				slug: 'evidence-matrix',
				enFile: 'CODEX_NON_VERIFIABLE_REPORTS_EVIDENCE_MATRIX.md',
				esFile: 'CODEX_NON_VERIFIABLE_REPORTS_EVIDENCE_MATRIX.es.md'
			}
		]
	}
];

export function getThread(slug: string): Thread | undefined {
	return threads.find((t) => t.slug === slug);
}

export function getThreadDoc(thread: Thread, docSlug: string): ThreadDoc | undefined {
	return thread.docs.find((d) => d.slug === docSlug);
}

export type PageEntry = { thread: string; doc?: string; lang: Lang };

export function allPageEntries(): PageEntry[] {
	const entries: PageEntry[] = [{ thread: '', lang: 'en' }];

	for (const thread of threads) {
		entries.push({ thread: thread.slug, lang: 'en' });
		entries.push({ thread: thread.slug, lang: 'es' });
		for (const doc of thread.docs) {
			entries.push({ thread: thread.slug, doc: doc.slug, lang: 'en' });
			entries.push({ thread: thread.slug, doc: doc.slug, lang: 'es' });
		}
	}

	return entries;
}
