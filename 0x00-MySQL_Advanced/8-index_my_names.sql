-- 8. Optimize simple search
-- Create index on first letter of name

CREATE INDEX idx_name_first ON names(name(1));

