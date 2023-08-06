module ford_example_type_mod
  implicit none

  private

  type, public :: example_type
    !! Some type that can say hello.
    !!
    !! This type's docs demonstrate how documentation is rendered
    !! differently for public/private components, and for type-bound
    !! procedure bindings and the procedures themselves.
    private
    integer :: counter = 1
    !! Internal counter
    character(len=:), allocatable, public :: name
    !! Name of this instance
  contains
    procedure :: say_hello => example_type_say
    !! This will document the type-bound procedure *binding*, rather
    !! than the procedure itself. The specific procedure docs will be
    !! rendered on the `example_type` page.
  end type example_type

contains

  subroutine example_type_say(self)
    !! Prints how many times this instance has said hello
    !!
    !! This subroutine has more documentation that won't appear in the
    !! summary in the procedure list, but should appear in the type
    !! page.
    class(example_type), intent(in) :: self
    write(*, '(a, " has said hello ", i0, " times.")') self%name, self%counter
    self%counter = self%counter + 1
  end subroutine example_type_say

end module ford_example_type_mod
