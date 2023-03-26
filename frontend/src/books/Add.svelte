  <div>
   <button><a href='#/books/'>Books</a></button>
    <h1>Add Book</h1>
    <form on:submit|preventDefault="{handleSubmit}">
      <label>
        Name:
        <input type="text" bind:value="{name}">
      </label>
      <label>
      <button type="submit">Submit</button>
    </form>
  </div>

<script>

  import jwt_decode from "jwt-decode";
  let name = '';
  export let apiUrl = 'http://localhost:8000/graphql/';
  
  const token = localStorage.getItem('token');
  async function handleSubmit() {
    let query = `
      mutation createBook($name: String!) {
        createBook(name: $name) {
          book{
            id,
            name
          }
        }
      }
    `; 
    const variables = { name };
    
    try {
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${token}`,
        },
        body: JSON.stringify({ query, variables })
      });

      const data = await response.json();
      window.location.href = '/#/books';
    } catch (error) {
      console.error(error);
    }
  }
</script>
