<script>
  import Router from "svelte-spa-router";
  import link from "svelte-spa-router";
  import Home from "./Home.svelte";
  import Login from "./Login.svelte";
  import Register from "./Register.svelte";
  
    const routes = {
      "/": Home,
      "/login": Login,
      "/register": Register 
    };
</script>

<nav>
  <ul>
    <li><a href="/#" use:link>Home</a></li>
    <li><a href="#/login" use:link>Login</a></li>
    <li><a href="#/register" use:link>Register</a></li>
  </ul>
</nav>

<Router {routes}/>
