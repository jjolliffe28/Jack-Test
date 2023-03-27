IF [Level 2] = "Real Estate" THEN [Cmt] ELSE WINDOW_SUM(SUM([Cmt])) - SUM(IF [Level 2] = "Real Estate" THEN [Cmt] END) END
