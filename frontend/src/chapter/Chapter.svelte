<script>
  import { onMount } from 'svelte';
    import { getCookie } from '../utils';


  const token = getCookie('token');

  async function fetchUserData(apiUrl, token, query) {
    const resp = await fetch(apiUrl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify({ query })
    });

    const { data } = await resp.json();
    return data.chapter;
  }

let chapter;
let chapterId;
let bookId;
  onMount(async () => {
    if (token) {
      const apiUrl = 'http://localhost:8000/graphql/';
      const url = window.location.href;
      let segment = url.split('/');
      bookId = segment[segment.length-3]
      chapterId = segment[segment.length - 1];
      const query = `query{chapter(bookId: ${bookId}, chapterId:${chapterId}){id, name, textContent, order, book{author{username}}}}`;
      chapter = await fetchUserData(apiUrl, token, query);
    }
  });
</script>

{#if chapter}
<p>
  {chapter.name} - By <i>"{chapter.book.author.username}"</i>
  <a href="/#/book/{bookId}/chapter/edit/{chapter.order}">Edit</a>
  <a href="/#/book/{bookId}/chapter/delete/{chapter.order}">Delete</a>
  {chapter.textContent}
</p>
{/if}
