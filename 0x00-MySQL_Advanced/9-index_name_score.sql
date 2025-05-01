-- 9. Optimize search and score
-- Create compound index on name first letter and score

CREATE INDEX idx_name_first_score ON names(name(1), score);
