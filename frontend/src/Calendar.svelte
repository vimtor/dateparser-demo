<script>
    export let date = new Date()
    import formatDate from 'dateformat'
    import calendarize from "calendarize";

    const weekdays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    const view = calendarize(date)
    const days = view.flat()
</script>

<div>
    <header>{formatDate(date, 'mmmm yyyy')}</header>
    <div class="grid" role="list">
        {#each weekdays as day}
            <div class="weekday">{day}</div>
        {/each}
        {#each days as day}
            <div class="item" role="listitem" class:selected={date.getDate() === day}>
                {day ? day : ""}
            </div>
        {/each}
    </div>
</div>

<style>
    .grid {
        display: grid;
        grid-template-columns: repeat(7, 36px);
    }

    .item {
        border: 1px solid lightgray;
        height: 36px;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 0.75rem;
    }

    .weekday {
        text-align: center;
        padding: 0.5em 0;
        font-size: 0.75rem;
    }

    .selected {
        color: white;
        background-color: hsl(358, 90%, 45%);
        border-color: hsl(358, 90%, 45%);
    }

    header {
        text-align: center;
        margin-bottom: 0.5em;
    }
</style>
