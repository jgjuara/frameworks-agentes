<script lang="ts">
	import { onMount } from 'svelte';
	import { createNoise2D } from 'simplex-noise';

	type Blob = {
		id: number;
		path: string;
		side: 'left' | 'right';
		top: number;
		opacity: number;
		visible: boolean;
	};

	let blobs = $state<Blob[]>([]);
	let nextId = 0;

	function randomRange(min: number, max: number): number {
		return min + Math.random() * (max - min);
	}

	function organicPath(): string {
		const cx = randomRange(40, 80);
		const cy = randomRange(40, 80);
		const r = randomRange(28, 55);
		const points = 6 + Math.floor(Math.random() * 3);
		const coords: { x: number; y: number }[] = [];

		for (let i = 0; i < points; i++) {
			const angle = (i / points) * Math.PI * 2;
			const wobble = randomRange(0.65, 1.15);
			coords.push({
				x: cx + Math.cos(angle) * r * wobble,
				y: cy + Math.sin(angle) * r * wobble
			});
		}

		let d = `M ${coords[0].x} ${coords[0].y}`;
		for (let i = 0; i < points; i++) {
			const curr = coords[i];
			const next = coords[(i + 1) % points];
			const midX = (curr.x + next.x) / 2 + randomRange(-8, 8);
			const midY = (curr.y + next.y) / 2 + randomRange(-8, 8);
			d += ` Q ${curr.x + randomRange(-6, 6)} ${curr.y + randomRange(-6, 6)} ${midX} ${midY}`;
		}
		d += ' Z';
		return d;
	}

	function blobColor(): string {
		return 'hsl(42, 18%, 72%)';
	}

	function wait(ms: number): Promise<void> {
		return new Promise((resolve) => setTimeout(resolve, ms));
	}

	onMount(() => {
		const noise = createNoise2D();
		let time = 0;
		let cancelled = false;

		async function cycle() {
			while (!cancelled) {
				time += 0.37;
				const intervalMs = 8000 + noise(time, 0) * 12000 + noise(0, time) * 4000;
				await wait(Math.max(4000, intervalMs));
				if (cancelled) break;

				const id = nextId++;
				const fadeInMs = randomRange(4000, 8000);
				const holdMs = randomRange(3000, 8000);
				const fadeOutMs = randomRange(4000, 8000);
				const maxOpacity = randomRange(0.06, 0.12);

				const blob: Blob = {
					id,
					path: organicPath(),
					side: Math.random() > 0.5 ? 'left' : 'right',
					top: randomRange(8, 82),
					opacity: 0,
					visible: true
				};

				blobs = [...blobs, blob];

				const fadeInSteps = 40;
				for (let s = 1; s <= fadeInSteps; s++) {
					if (cancelled) return;
					const t = s / fadeInSteps;
					const eased = t * t * (3 - 2 * t);
					blobs = blobs.map((b) =>
						b.id === id ? { ...b, opacity: maxOpacity * eased } : b
					);
					await wait(fadeInMs / fadeInSteps);
				}

				await wait(holdMs);
				if (cancelled) break;

				const fadeOutSteps = 40;
				for (let s = fadeOutSteps; s >= 0; s--) {
					if (cancelled) return;
					const t = s / fadeOutSteps;
					const eased = t * t * (3 - 2 * t);
					blobs = blobs.map((b) =>
						b.id === id ? { ...b, opacity: maxOpacity * eased } : b
					);
					await wait(fadeOutMs / fadeOutSteps);
				}

				blobs = blobs.filter((b) => b.id !== id);
			}
		}

		cycle();

		return () => {
			cancelled = true;
		};
	});
</script>

<div class="peripheral-layer" aria-hidden="true">
	{#each blobs as blob (blob.id)}
		<svg
			class="peripheral-blob"
			class:left={blob.side === 'left'}
			class:right={blob.side === 'right'}
			style:top="{blob.top}%"
			style:opacity={blob.opacity}
			viewBox="0 0 120 120"
			xmlns="http://www.w3.org/2000/svg"
		>
			<path d={blob.path} fill={blobColor()} />
		</svg>
	{/each}
</div>

<style>
	.peripheral-layer {
		position: fixed;
		inset: 0;
		pointer-events: none;
		z-index: 0;
		overflow: hidden;
	}

	.peripheral-blob {
		position: absolute;
		width: min(10vw, 7rem);
		height: min(10vw, 7rem);
		transition: opacity 0.15s linear;
	}

	.peripheral-blob.left {
		left: min(2vw, 1.5rem);
	}

	.peripheral-blob.right {
		right: min(2vw, 1.5rem);
	}
</style>
