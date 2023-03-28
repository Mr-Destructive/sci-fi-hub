<div>
  <h3>Are you sure want to delete this chapter</h3>
  <form on:submit|preventDefault="{handleSubmit}">
      Name: {name}
      Order: {order}
      Status: {status}
    <button type="submit">Delete</button>
  </form>
</div>

<script>
  import { apiUrl, getCookie } from "../utils.js"
  const url = window.location.href;
  let segment = url.split('/');
  let bookId = parseInt(segment[segment.length - 4]);
  let chapterId = parseInt(segment[segment.length - 1]);
  let name = '';
  let query;
  let textContent = '';
  let order = 0;
  let status = false;

  async function fetchChapter() {
    query = `
      query chapters($bookId: ID!, $chapterId: ID!) {
        chapter(bookId: $bookId, chapterId: $chapterId) {
          id
          name
          textContent
          order
          status
        }
      }
    `;
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
    const data = await response.json();
    const chapter = data.data.chapter;

    name = chapter.name;
    textContent = chapter.textContent;
    order = chapter.order;
    status = chapter.status;
  }

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
    const data = await response.json();
    window.location.href = `/#/book/${bookId}/`;
  }

  fetchChapter();
</script>
