<script>
  import jwt from 'jsonwebtoken';
  import { useForm, validators, HintGroup, Hint,  required } from "svelte-use-form";

  const form = useForm();

  async function handleSubmit() {
    const apiUrl = 'http://localhost:8000/graphql/';
    const variables = { username, password};
    const query = `mutation TokenAuth($username: String!, $password: String!) {
      tokenAuth(username: $username, password: $password) {
        token
        payload
        refreshExpiresIn
      }
    }`;

    const response = await fetch(apiUrl, {
      method: 'POST',
      body: JSON.stringify({ query, variables }),
      headers: { 'Content-Type': 'application/json' }
    });

    const data = await response.json();
    localStorage.setItem('token', data.token);
    //const decodedToken = jwt.decode(data.token);
    //console.log(decodedToken);
  }
</script>

<form use:form on:submit|preventDefault={handleSubmit}>
  <h1>Login</h1>

  <input type="string" name="username" use:validators={[required ]} />
  <HintGroup for="username">
    <Hint on="required">This is a mandatory field</Hint>
  </HintGroup>

  <input type="password" name="password" use:validators={[required]} />
  <Hint for="password" on="required">This is a mandatory field</Hint>

  <button disabled={!$form.valid}>Login</button>
</form>

<pre>
</pre>

<style>
	:global(.touched:invalid) {
		border-color: red;
		outline-color: red;
	}
</style>
