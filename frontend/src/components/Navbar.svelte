<script>
    import jwtDecode from "jwt-decode";
    import { link } from "svelte-spa-router";
    import Router from "svelte-spa-router";
    import Home from "./Home.svelte";
    import Login from "./Login.svelte";
    import Logout from "./Logout.svelte";
    import Register from "./Register.svelte";
    import Books from "../books/List.svelte";
    import Book from "../books/Book.svelte";
    import AddBook from "../books/Add.svelte";
    import { getCookie } from "../utils";
    import Chapters from "../chapter/List.svelte";
    import Chapter from "../chapter/Chapter.svelte";
    import AddChapter from "../chapter/Add.svelte";
    import EditChapter from "../chapter/Edit.svelte"
    import DeleteChapter from "../chapter/Delete.svelte"
    let auth;
    let token = getCookie('token')
    if (token && token !== 'null') {
        let user = jwtDecode(token)
        if (user.username){
            auth = true
        }
    }
    const routes = {
      "/": Home,
      "/login": Login,
      "/logout": Logout,
      "/register": Register,
      "/books": Books,
      "/book/:id": Book,
      "/add/books": AddBook,
      "/chapter/": Chapters,
      "/book/:id/chapter/:id": Chapter,
      "/book/:id/chapter/edit/:id": EditChapter,
      "/book/:id/chapter/delete/:id": DeleteChapter,
      "/add/chapter/": AddChapter,
    };
</script>
<ul>
    <li><a href="#/" use:link>Home</a></li> |
    {#if auth}
        <li><a href="#/logout" use:link>Logout</a></li>
    {:else}
        <li><a href="#/register" use:link>Register</a></li> |
        <li><a href="#/login" use:link>Login</a></li>
    {/if}
</ul>
<Router {routes}/>

<style>
	ul>li{
		display : inline;
	}
</style>
