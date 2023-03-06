<script>
    const apiUrl = 'http://localhost:8000/';
    const query = '{authors{id,username}}';
    const endpoint = `${apiUrl}?query=${encodeURIComponent(query)}`
  import { onMount, afterUpdate } from 'svelte';

  let element;

  function handleElementChange() {
    console.log('Element has changed!');
  }

  onMount(() => {
    element.addEventListener('change', handleElementChange);
  });

    afterUpdate(() => {
        if (element.value) {
          previousValue = element.value;
          console.log('Element value has changed!');
        }
      });
</script>

<button _="on click fetch `{endpoint}` then
                    put the result as an JSON 
                    into next <p/> ">
  Get authors
</button>

    <p id="authors" bind:this={element} ></p>
