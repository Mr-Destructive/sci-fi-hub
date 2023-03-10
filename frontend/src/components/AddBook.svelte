<script>
  let name = '';
  let error = null;
  
  const addBook = async () => {
    const query = `mutation CreateBook($name: String!) {
          createBook(name: $name) {
            book {
              name
              author {
                username
              }
            }
          }
        }`;
    
    const variables = { name,};
    const apiUrl = 'http://localhost:8000/graphql/';
    
    const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer yJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjc4Mjc2OTY3LCJvcmlnSWF0IjoxNjc4Mjc2NjY3fQ.U6dp5OdV0WohYCudvTwLdxtmVE6egyiZBqcQR_l10XI'
        },
        body: JSON.stringify({ query, variables })
    });
    
    const data = await response.json();
    
    if (data.errors || response.status !== 200) {
      error = data.errors[0].message;
    } else {
      name = '';
      error = null;
    }
  };
</script>

<main>
  <h1>Add a New Book</h1>
  
  {#if error}
    <p style="color: red;">{error}</p>
  {/if}
  
  <form on:submit|preventDefault={addBook}>
    <div>
      <label for="name">Name:</label>
      <input type="text" id="name" bind:value={name} required />
    </div>
    
  </form>
</main>
    
