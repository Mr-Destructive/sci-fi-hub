<script>
    import h from 'hyperscript';

    const apiUrl = 'http://localhost:8000/';
    const query = '{authors{id,username}}';
    const endpoint = `${apiUrl}?query=${encodeURIComponent(query)}`
</script>
<button _="on click fetch `{endpoint}` then
                    put the result as an JSON 
                    into next <p/> ">
  Get authors
</button>

<p id="authors"></p>
