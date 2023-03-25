import App from './App.svelte';

const app = new App({
	target: document.body,
	props: {
		name: 'SciFi Hub',
        apiUrl: 'http://localhost:8000/graphql/'
	}
});
export default app;
