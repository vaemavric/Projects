class PagesController < ApplicationController
	def home
		@students = Student.all
	end
end
