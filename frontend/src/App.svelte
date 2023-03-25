<script>
    import AddBook from "./components/AddBook.svelte";
    import Api from "./components/API.svelte";
    import Login from "./components/Login.svelte";
    import LoginPage from "./components/LoginPage.svelte";
	export let name;
	export let menu = 1;
</script>

<main>
    <ul id="menu">
        <li><a href="/" on:click|preventDefault={() => (menu = 1)}>Login</a></li>
        <li><a href="/" on:click|preventDefault={() => (menu = 2)}>Books</a></li>
    </ul>

    {#if menu === 1}
    <Login/>
    {:else if menu === 2}
    <AddBook/>
    {:else}
    <h1>
        Page Not Found
    </h1>
    {/if}
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>
