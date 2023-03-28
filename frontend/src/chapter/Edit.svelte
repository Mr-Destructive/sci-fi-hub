<div>
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

<script>
  import { apiUrl, getCookie } from "../utils.js"
  const url = window.location.href;
  let segment = url.split('/');
  let chapterId = parseInt(segment[segment.length - 1]);
  let bookId = parseInt(segment[segment.length-4]);
  console.log(bookId)
  console.log(chapterId)
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
    console.log(data)
    const chapter = data.data.chapter;

    name = chapter.name;
    textContent = chapter.textContent;
    order = chapter.order;
    status = chapter.status;
  }

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
    console.log(data)
    let chapter_order = data.data.updateChapter.chapter.order
    console.log(data.data.updateChapter.chapter)
    window.location.href = `/#/book/${bookId}/chapter/${chapter_order}`;
  }

  fetchChapter();
</script>
