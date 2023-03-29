<script>
  let render = false;
  function render_form(){
    console.log(render)
    render = true;
  }
  export let bookId
  import { apiUrl, getCookie } from "../utils.js"
  export let chapter;
  let componentRef;
  function bindComponent(ref) {
    componentRef = ref;
  }
  const url = window.location.href;
  let segment = url.split('/');
  let chapterId = parseInt(segment[segment.length - 1]);
  //bookId = parseInt(segment[segment.length-4]);
  let name = '';
  let query;
  let textContent = '';
  let order = 0;
  let status = false;
    name = chapter.name;
    textContent = chapter.textContent;
    order = chapter.order;
    status = chapter.status;

  async function handleSubmit() {
    query = `
      mutation updateChapter($bookId: ID!, $chapterId: ID!, $name: String!, $textContent: String!, $order: Int!, $status: Boolean!) {
        updateChapter(bookId: $bookId, chapterId: $chapterId, name: $name, textContent: $textContent, order: $order, status: $status) {
          chapter {
            id
            name
            textContent
            order
            status
            book{
              author{
                username
              }
            }
          }
        }
      }
    `;
    let token = getCookie('token');

    const variables = { bookId, chapterId, name, textContent, order, status };
    const response = await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
      },
      body: JSON.stringify({ query, variables })
    });
    const data = await response.json();
    if (response.status === 200){
    let chapter_order = data.data.updateChapter.chapter.order
    chapter = data.data.updateChapter.chapter
    render = false;
    window.location.href = `/#/book/${bookId}/chapter/${chapter_order}`;
    }
  }

</script>

{#if !render}
    <button on:click={render_form}>Edit</button>
{:else }
<div>
{render}
  <a href='#/books/'><button>Books</button></a>
  <h1>Update Chapter</h1>
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
      <input type="text" bind:value="{status}">
    </label>
    <button type="submit">Update</button>
  </form>
</div>
{/if}
