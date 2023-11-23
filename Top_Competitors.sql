SELECT s.hacker_id, h.name FROM Submissions s 
LEFT JOIN Challenges c ON s.challenge_id = c.challenge_id 
LEFT JOIN Difficulty d ON c.difficulty_level = d.difficulty_level
LEFT JOIN Hackers h ON h.hacker_id = s.hacker_id 
WHERE s.score=d.score GROUP BY s.hacker_id, h.name 
HAVING count(submission_id)>1
ORDER BY count(submission_id) DESC, hacker_id;