class CreateStudents < ActiveRecord::Migration[5.0]
  def change
    create_table :students do |t|

      t.string :name
	  t.string :cuid
	  t.string :created
	  t.string :updated
    end
  end
end
