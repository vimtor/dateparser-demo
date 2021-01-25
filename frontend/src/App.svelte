<script>
    const endpoint = 'http://localhost:5000';

    let date = new Date()
    let text = ''

    const handleSubmit = async event => {
        event.preventDefault()
        const response = await fetch(`${endpoint}?text=${encodeURI(text)}`);
        if (response.ok) {
            const dateText = await response.text()
            date = new Date(dateText)
        }
        else {
            // TODO: Invalid date logic
        }
    };
</script>

<main>
    <form on:submit={handleSubmit}>
        <label>
            Text:
            <input type="text" bind:value={text}>
        </label>
        <button>Submit</button>
    </form>
    <pre>{date.toString()}</pre>
</main>

<style>
</style>
