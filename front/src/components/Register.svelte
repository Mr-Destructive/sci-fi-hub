  <div class="register-form">
    <h2>Register</h2>
    <form on:submit|preventDefault={handleRegister}>
      <label for="email">Email:</label>
      <input type="email" id="email" bind:value={email} />

      <label for="username">Username:</label>
      <input type="text" id="username" bind:value={username} />

      <label for="password">Password:</label>
      <input type="password" id="password" bind:value={password} />

      <button type="submit">Register</button>
    </form>

  </div>

<script>
  import { goto } from '@sapper/app';
  let email = '';
  let username = '';
  let password = '';
  export let apiUrl = 'http://localhost:8000/graphql/';

  async function handleRegister() {
    const query = `
      mutation CreateAuthor($email: String!, $username: String!, $password: String!) {
        createAuthor(email: $email, username: $username, password: $password) {
          token,
          refreshToken,
          author{
          id,
          username
          }
        }
      }
    `;
    const variables = { email, username, password };

    try {
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({query, variables})
      });

      if (!response.ok) {
        throw new Error('Registration failed');
      }else{
        //TODO: fix goto from sapper
        window.location.href = '/#/login';
      }
    } catch (error) {
      console.error(error);
    }
  }
</script>

<style>
  .register-form {
    max-width: 400px;
    margin: 0 auto;
    padding: 2rem;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
  }

  h2 {
    text-align: center;
  }

  form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    margin-top: 1rem;
  }

  label {
    font-weight: bold;
  }

  input {
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 3px;
    font-size: 1rem;
  }

  button {
    padding: 0.5rem 1rem;
    background-color: #2b2d42;
    color: #fff;
    border: none;
    border-radius: 3px;
    cursor: pointer;
  }
</style>
