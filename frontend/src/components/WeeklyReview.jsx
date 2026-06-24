function WeeklyReview({
  summary
}) {

  return (

    <div>

      <h2>Weekly Review</h2>

      {summary.map(
        (item, index) => (

          <p key={index}>
            {item}
          </p>

        )
      )}

    </div>

  );
}

export default WeeklyReview;