<script>
  let render = false;
  import { apiUrl, getCookie } from "../utils.js"
  function render_form(){
    render = true;
  }
  export let bookId
  const url = window.location.href;
  let segment = url.split('/');
  let chapterId = parseInt(segment[segment.length - 1]);
  let name = '';
  let query;
  let order = 0;
  let status = false;

  async function handleSubmit() {
    query = `mutation delete_chapter{
      deleteChapter(bookId: ${bookId}, chapterId: ${chapterId}){
        success
      }
    }`;
    let token = getCookie('token');

    const variables = { bookId, chapterId };
    const response = await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
      },
      body: JSON.stringify({ query, variables })
    });
    window.location.href = `/#/book/${bookId}`;
  }

</script>

{#if !render}
    <button on:click={render_form}>Delete</button>
{:else }
    <div>
      <h3>Are you sure want to delete this chapter</h3>
      <form on:submit|preventDefault="{handleSubmit}">
          Name: {name}
          Order: {order}
          Status: {status}
        <button type="submit">Delete</button>
      </form>
    </div>
{/if}
