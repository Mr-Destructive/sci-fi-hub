<div>
   <a href='#/books/'><button>Books</button></a>
    <h1>Add Chapter</h1>
    <form on:submit|preventDefault="{handleSubmit}">
      <label>
        Name:
        <input type="text" bind:value="{name}">
      </label>
      <label>
        Content:
        <textarea bind:value="{textContent}"></textarea>
      </label>
      <label>
        Order:
        <input type="number" bind:value="{order}">
      </label>
      <label>
        Status:
        <input type="text">
      </label>
      <button type="submit">Submit</button>
    </form>
</div>
<script>
  import { apiUrl, getCookie } from "../utils.js"
  const url = new URLSearchParams(window.location.hash.split('?')[1]);
  let bookId = url.get('bookId');
  let name;
  let query;
  let textContent;
  let order;
  let status = false;

  async function handleSubmit() {

query = `mutation createChapter($name: String!, $textContent: String!, $order: Int!, $bookId: ID!, $status: Boolean!) {
  createChapter(name: $name, bookId: $bookId, textContent: $textContent, order: $order, status: $status) {
    chapter {
      order
      name
      id
    }
  }
}`;
const variables = { name, bookId, order, status, textContent};
  let token = getCookie('token');

    
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
